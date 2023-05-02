import asyncio


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    print(f"{cmd!r} exited with {proc.returncode}")
    if stdout:
        print(stdout.decode())
    else:
        print("NO STDOUT")
    if stderr:
        print(stderr.decode())
    else:
        print("NO ERROR")


async def main():
    await asyncio.gather(
        run("echo Hello World"),
        run("dir"),
        run("ls -1 -r d:\\"),
    )


asyncio.run(main())
# asyncio.run(run('echo Hello World'))
