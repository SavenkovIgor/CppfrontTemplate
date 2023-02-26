#!/usr/bin/env python3

import subprocess
import argparse
from pathlib import Path


def repository_root() -> Path:
    return Path(__file__).parent


def system_call(command: str):
    if subprocess.call(command, shell=True, executable='/bin/bash') != 0:
        exit(1)


def delete_if_exist(path: Path):
    if path.exists():
        print(f'Delete {path}')
        system_call(f'rm -rf {path}')


class Project:
    def root_dir(self) -> Path:
        return Path(__file__).parent

    def name(self) -> str:
        return self.root_dir().name

    def build_dir(self) -> Path:
        return self.root_dir() / 'build'

    def install(self):
        print(f'---INSTALL {self.name()}---')
        system_call(f'conan install -if ./conanfiles -pr:b=default --build=missing ./')

    def build(self):
        self.install()
        print(f'---BUILD {self.name()}---')
        system_call(f'conan build -if ./conanfiles -bf ./build ./')

    def run(self):
        print(f'---RUN {self.name()}---')
        system_call(f'./build/cpp_template')

    def clear(self, clear_conan: bool = False):
        # rm -rf ./build ./conanfiles
        print(f'---CLEAR {self.name()}---')
        delete_if_exist(self.build_dir())
        delete_if_exist(self.root_dir() / 'conanfiles')

        if clear_conan:
            system_call('conan remove -f "*"')


def main():
    parser = argparse.ArgumentParser(description='Project build script')

    parser.add_argument('--install',     action='store_true', help='Install dependencies')
    parser.add_argument('--build',       action='store_true', help='Build project')
    parser.add_argument('--run',         action='store_true', help='Run project')
    parser.add_argument('--clear',       action='store_true', help='Clear project')
    parser.add_argument('--clear-all',   action='store_true', help='Clear project and conan cache')

    args = parser.parse_args()

    app = Project()

    if args.install:
        app.install()

    if args.build:
        app.build()

    if args.run:
        app.run()

    if args.clear:
        app.clear()

    if args.clear_all:
        app.clear(clear_conan=True)


if __name__ == '__main__':
    main()
