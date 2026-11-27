"""Compare word suggestions and protect maths notation in an Assamese fraction exercise.

Install numpy, requests and onnxruntime. Run with Python 3.10 or later.
The downloaded ONNX files stay in the user's normal temporary directory.
"""
import json
from pathlib import Path
import re
import tempfile
import unicodedata
import numpy as np
import onnxruntime as ort
import requests

REV = "c4065f395489f928cec58ca9a1840f68589a4b9b"
MODEL = "aaiiaxom/indicxlit-roman-to-assamese-onnx-int8"
FILES = ("encoder.int8.onnx", "decoder.int8.onnx", "model_config.json", "src_vocab.json", "tgt_vocab.json")
WORDS = ("bhognangsho", "lob", "lab", "hor", "har", "jog", "biyog", "dui", "tini", "chari")

def run():
    folder = Path(tempfile.gettempdir()) / ("modumath-indicxlit-" + REV)
    folder.mkdir(exist_ok=True)
    for name in FILES:
        dest = folder / name
        if not dest.exists():
            response = requests.get(f"https://huggingface.co/{MODEL}/resolve/{REV}/{name}", timeout=30)
            response.raise_for_status()
            temp = dest.with_suffix(".part")
            temp.write_bytes(response.content)
            temp.replace(dest)
    cfg, src, tgt = [json.loads((folder / f).read_text(encoding="utf-8")) for f in FILES[2:]]
    src_ids = {char: index for index, char in enumerate(src)}
    options = ort.SessionOptions()
    options.intra_op_num_threads = 1
    options.inter_op_num_threads = 1
    enc, dec = [ort.InferenceSession(str(folder / n), sess_options=options,
                providers=["CPUExecutionProvider"]) for n in FILES[:2]]
    def suggest(word):
        ids = [cfg["src_lang_token_idx"], *(src_ids[c] for c in word), cfg["src_eos_idx"]]
        states, mask = enc.run(None, {"src_tokens": np.array([ids], dtype=np.int64)})
        tokens = [cfg["decoder_start_token_idx"]]
        for _ in range(32):
            logits, = dec.run(None, {"prev_output_tokens": np.array([tokens], dtype=np.int64),
                                     "encoder_out": states, "encoder_padding_mask": mask})
            scores = logits.reshape(-1).copy()
            scores[[cfg["tgt_pad_idx"], cfg["tgt_unk_idx"]]] = -np.inf
            best = int(scores.argmax())
            if best == cfg["tgt_eos_idx"]:
                break
            tokens.append(best)
        return unicodedata.normalize("NFC", "".join(tgt[i] for i in tokens[1:]
                  if not tgt[i].startswith(("<", "__"))))

    suggestions = {word: suggest(word) for word in WORDS}
    # Only recognised lesson labels can request a suggestion. The exercise stores
    # its formula separately; never pass a variable, fraction or operator to the model.
    def render(label, formula):
        if not re.fullmatch("[a-z]+", label) or label not in suggestions:
            raise ValueError("Select a lesson label")
        return suggestions[label], formula

    for label, formula in (("lob", "3/4"), ("hor", "৩/৪"), ("jog", "x + 1/4")):
        result = render(label, formula)
        assert result[1].encode("utf-8") == formula.encode("utf-8")
        print(f"{label!r} -> {result[0]!r} | {result[1]}")
    print(json.dumps(suggestions, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    run()
