beta_code_mapping = {
    # Simple mappings
    ' ': ' ',

    'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd', 'ε': 'e', 'ζ': 'z', 'η': 'h', 'θ': 'q',
    'ι': 'i', 'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'c', 'ο': 'o', 'π': 'p',
    'ρ': 'r', 'σ': 's', 'ς': 's', 'τ': 't', 'υ': 'u', 'φ': 'f', 'χ': 'x', 'ψ': 'y', 'ω': 'w',

    # Capital letters
    'Α': '*a', 'Β': '*b', 'Γ': '*g', 'Δ': '*d', 'Ε': '*e', 'Ζ': '*z', 'Η': '*h', 'Θ': '*q',
    'Ι': '*i', 'Κ': '*k', 'Λ': '*l', 'Μ': '*m', 'Ν': '*n', 'Ξ': '*c', 'Ο': '*o', 'Π': '*p',
    'Ρ': '*r', 'Σ': '*s', 'Τ': '*t', 'Υ': '*u', 'Φ': '*f', 'Χ': '*x', 'Ψ': '*y', 'Ω': '*w',

    # Vowels with diacritics
    'ὰ': 'a)', 'ά': 'a/', 'ᾶ': 'a=', 'ἀ': 'a(', 'ἁ': 'a(/', 'ἄ': 'a(/', 'ἅ': 'a(/', 
    'ἆ': 'a(=', 'ἇ': 'a(=',
    'ὲ': 'e)', 'έ': 'e/', 'ἐ': 'e(', 'ἑ': 'e(/', 'ἔ': 'e(/', 'ἕ': 'e(/',
    'ὴ': 'h)', 'ή': 'h/', 'ῆ': 'h=', 'ἠ': 'h(', 'ἡ': 'h(/', 'ἤ': 'h(/', 'ἥ': 'h(/', 
    'ἦ': 'h(=', 'ἧ': 'h(=',
    'ὶ': 'i)', 'ί': 'i/', 'ῖ': 'i=', 'ἰ': 'i(', 'ἱ': 'i(/', 'ἴ': 'i(/', 'ἵ': 'i(/', 
    'ἶ': 'i(=', 'ἷ': 'i(=',
    'ὸ': 'o)', 'ό': 'o/', 'ὀ': 'o(', 'ὁ': 'o(/', 'ὄ': 'o(/', 'ὅ': 'o(/',
    'ὺ': 'u)', 'ύ': 'u/', 'ῦ': 'u=', 'ὐ': 'u(', 'ὑ': 'u(/', 'ὔ': 'u(/', 'ὕ': 'u(/', 
    'ὖ': 'u(=', 'ὗ': 'u(=',
    'ὼ': 'w)', 'ώ': 'w/', 'ῶ': 'w=', 'ὠ': 'w(', 'ὡ': 'w(/', 'ὤ': 'w(/', 'ὥ': 'w(/', 
    'ὦ': 'w(=', 'ὧ': 'w(=',

    # Additions for diaeresis and some punctuation
    'ϊ': 'i+', 'ϋ': 'u+', 'ῒ': 'i+)', 'ῢ': 'u+)', 'ῗ': 'i+=', 'ῧ': 'u+=',
    '·': '.',  # Ano teleia (Greek semicolon)
    ';': '?',  # Greek question mark is represented by a semicolon in Greek script
    'ᾳ': 'a|', 'ῃ': 'h|', 'ῳ': 'w|',  # Iota subscripts
    'ᾴ': 'a/|', 'ῄ': 'h/|', 'ῴ': 'w/|',  # Iota subscript with acute
    'ᾲ': 'a)|', 'ῂ': 'h)|', 'ῲ': 'w)|',  # Iota subscript with grave
    'ᾷ': 'a=|', 'ῇ': 'h=|', 'ῷ': 'w=|'  # Iota subscript with circumflex

}