def process(data: str) -> list:
    rows = split_string(data, "\n", True)
    title_row = split_string(rows[0], ",")

    output_list = []

    for i, row in enumerate(rows[1:]):
        csv_row = {}
        for j, item in enumerate(split_string(row, ",")):
            csv_row[title_row[j]] = item
        output_list.append(csv_row)

    for row in output_list:
        print(row)

    return output_list

def split_string(string_to_split: str, separator: str, ignore_single_quotes = False) -> list[str]:
    output = []
    substring = ""
    in_quotation = False

    i = 0
    while i < len(string_to_split):
        char = string_to_split[i]
        if char == "\r":
            i += 1
            continue
        if char == '"':
            if i + 1 < len(string_to_split) and string_to_split[i + 1] == '"':
                substring += '"'
                i += 1
            else:
                in_quotation = not in_quotation
        if char == separator and not in_quotation:
            output.append(substring)
            substring = ""
        else:
            if ignore_single_quotes:
                substring += char
            else:
                if char != '"':
                    substring += char
        i += 1

    output.append(substring)

    return output

process('''ID,Name,Email,Comment,Amount,Date
1,John Doe,john@example.com,"Simple valid row",123.45,2025-10-01
2,"Jane, Smith",jane.smith@example.com,"Name includes comma",67.89,2025-10-02
3,"Liam ""The Wolf"" O'Brien",liam.obrien@example.com,"Embedded quotes using doubled quotes",10.00,2025-10-03
4,Emily Brown,emily.brown@example.com,"Multiline comment:
This is a second line.",42.00,2025-10-04
5," Müller, Max ",max.müller@example.de,"UTF-8 characters: äöüß€",500.00,2025-10-05
6,"Chen, Wei",chen.wei@example.cn,"Field with leading and trailing spaces ",321.00,2025-10-06
7,"Rossi, Maria",maria.rossi@example.it,"Trailing newline in quoted field
",250.00,2025-10-07
8,"Smith, Bob",bob.smith@example.com,"Contains CRLF line break\r\nwithin text",77.77,2025-10-08
9,"O’Connor, Saoirse",saoirse.o'connor@example.ie,"Unicode punctuation – curly quotes “ ”, dash —, ellipsis …",88.88,2025-10-09
10,"Dupont, Chloé",chloe.dupont@example.fr,"Emoji test: 😊🚀✨",99.99,2025-10-10
11," García, José ",jose.garcia@example.es,"Field with comma, quote, and newline:
""This, is tricky!""",111.11,2025-10-11
12,"Nørgaard, Lærke",laerke.norgaard@example.dk,"Nordic letters test: æøå",222.22,2025-10-12
13,"Tanaka, Yuki",tanaka.yuki@example.jp,"Japanese text: 東京, 日本語テスト",333.33,2025-10-13
14,"İpek, Çağla",cagla.ipek@example.tr,"Turkish characters: İ, ğ, ş, ç",444.44,2025-10-14
15,"Snow, Jon",jon.snow@example.com,"Quotes around empty field: """"",0.00,2025-10-15''')
