try:
    from importlib_metadata import version, PackageNotFoundError
    print(version("Flask"))
except PackageNotFoundError:
    print("Package not found.")


    def print_package_version(package: str):
        try:
            from importlib_metadata import version
            print(version(package))
        except PackageNotFoundError:
            print(f'Package "{package}" not found.')

            print_package_version("Flask")