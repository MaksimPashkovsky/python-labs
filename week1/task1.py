def ipv6_sum(ip: str):
    return "".join(
        [
            str(
                sum(
                    map(lambda x: int(x, 16), quad)
                )
            )
            for quad in ip.split(sep=ip[4])
        ]
    )


print(ipv6_sum("1111-1111-1111-1111-1111-1111-1111-1111"))