{ pkgs, stdenv, python3Packages, ... }:

python3Packages.buildPythonPackage {
  name = "thesola-io-api";
  pyproject = true;

  src = ./.;

  propagatedBuildInputs = with pkgs; with python3Packages;
  [ pylast
    flask
    flask-cors
    setuptools
    cachetools
    python-dotenv
  ];
}
