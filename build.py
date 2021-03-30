import os
import subprocess

PATCH = """
[patch.crates-io]
lmdb-rkv-sys = { git = "https://github.com/ForensicCat/lmdb-rs" }
"""


class BuildError(Exception):
    pass


def run(cmd: str) -> int:
    p = subprocess.Popen(cmd)
    r = p.wait()
    if r:
        raise BuildError(f'A Error raised when executing "{cmd}"')


os.mkdir("MeiliSearch")
os.chdir("MeiliSearch")

run("git clone https://github.com/meilisearch/MeiliSearch.git --depth=1 .")

with open("Cargo.toml", "a") as f:
    f.write(PATCH)

run("cargo build --release")
