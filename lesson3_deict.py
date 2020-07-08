ip = ()
asnumber = ()
uptime = ()
prefixnum = ()

bgpout = """10.197.0.46     4        64930   12113   16631  2176128    0    0 1d23h           3
10.197.0.58     4        64930   14801   17399  2176128    0    0 2d01h         184
10.197.0.67     4        64930    6507   11189  2176128    0    0 2d00h          10
10.197.0.69     4        64930   13598   17299  2176128    0    0 2d01h         398
10.197.0.70     4        64930   12135   16641  2176128    0    0 1d23h           4
10.197.0.71     4        64930   12125   16658  2176128    0    0 1d23h           3
10.197.35.16    4        64930   14203   16758  2176128    0    0 1d23h           5"""

for line in bgpout.splitlines():
    fields = line.split()
    ip = fields[0]
    asnumber = fields[2]
    uptime = fields[8]
    prefixnum = fields[9]

    selected_fields = {ip: {
        'asnumber': asnumber,
        'uptime': uptime,
        'prefixnum': prefixnum
    }
    }

    print(selected_fields)