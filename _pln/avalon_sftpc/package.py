
early = globals()["early"]


name = "avalon_sftpc"

description = "Avalon SFTP Client, for uploading Avalon workfile or " \
              "representation to remote site via SFTP"


@early()
def __payload():
    from earlymod import util
    return util.git_build_clone(
        url="https://github.com/davidlatwe/avalon-sftpc.git",
        branch="master",
    )


@early()
def version():
    import subprocess
    data = globals()["this"].__payload

    version_str = "0.3.0"  # (TODO) add version query
    branch_name = subprocess.check_output(
        ["git", "branch", "--show-current"],
        universal_newlines=True,
        cwd=data["repo"],
    ).strip()

    major, minor, patch = version_str.split(".")
    return "%s-%s.%s.%s" % (branch_name, major, minor, patch)


@early()
def authors():
    from earlymod import util
    data = globals()["this"].__payload
    return util.git_authors(data["repo"])


tools = [
    "python -m avalon_sftpc --demo",
]

requires = [
    # Dependencies
    "avalon",
    "pysftp",
]


private_build_requires = ["rezutil-1"]


@early()
def build_command():
    data = globals()["this"].__payload
    return "python -m rezutil build {root}".format(
        root=data["repo"],
    )


# Set up environment
def commands():
    env = globals()["env"]
    env.PYTHONPATH.prepend("{root}")
