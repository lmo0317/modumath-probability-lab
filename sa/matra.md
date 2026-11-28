<!--
author: ModuMath
language: hi
version: 1.0.0
comment: लघु और गुरु से चार, पाँच और छह मात्राओं के क्रम बनाइए।
-->

# लघु और गुरु से कितने क्रम बनेंगे?

In this counting game, L stands for a short syllable (लघु) of one mātrā, and G for a long one (गुरु) of two. Tap once for L and hold for two taps for G. Order matters: LG and GL have the same total length but sound different. This exercise counts all such strings, without adding the rules of a particular poetic metre.

## चार मात्राएँ · Four beats

चार मात्राओं का क्रम बनाइए। LLLL और GG के अलावा कितने अलग क्रम हैं? How many other patterns can you tap?

[( )] २ / Two
[(X)] ३ / Three
[( )] ५ / Five

तीन क्रमों में एक गुरु और दो लघु हैं: GLL, LGL, LLG। In each case the G occupies a different place. Together with LLLL and GG that makes five patterns.

## पाँच मात्राएँ · Five beats

पाँच मात्राओं में पहला वर्ण गुरु हो तो कितने क्रम होंगे? If the first syllable is long, how many patterns fit in five beats?

[( )] २ / Two
[(X)] ३ / Three
[( )] ५ / Five

पहला G दो मात्राएँ लेता है। शेष तीन मात्राओं में LLL, LG या GL रखें। The complete patterns are GLLL, GLG and GGL. If the first syllable is short instead, four beats remain and any of the five patterns from the first question will fit. In total: 3 + 5 = 8.

## छह मात्राएँ · Six beats

छह मात्राओं के सभी क्रम लिखे बिना उनकी संख्या निकालिए। Count the six-beat patterns without listing them all.

[( )] ८ / Eight
[( )] १२ / Twelve
[(X)] १३ / Thirteen

L से शुरुआत करने पर पाँच मात्राएँ बचती हैं, इसलिए ८ क्रम मिलते हैं। G से शुरुआत करने पर चार मात्राएँ बचती हैं, इसलिए ५ क्रम मिलते हैं। Every pattern starts with exactly one of L and G, so the two counts add to 13 without double-counting.

The [Vāk program](https://github.com/lmo0317/modumath-probability-lab/blob/main/sa/matra.vak) prints the actual patterns. ModuMath made this activity. To try a different topic, open our [English algebra example](https://math.hjinlabs.com/?lang=en&utm_source=vak_matra_lesson&utm_medium=resource&utm_campaign=india_math#/?section=practice).
