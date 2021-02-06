A, B, C = map(int, input().split())
print(
    "%d\n%d\n%d\n%d"
    % (
        ((A + B) % C),
        (((A % C) + (B % C)) % C),
        ((A * B) % C),
        (((A % C) * (B % C)) % C),
    )
)