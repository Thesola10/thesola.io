{ pkgs, stdenv, python3Packages, ... }:

python3Packages.buildPythonApplication {
  name = "thesola.io-api";
  pyproject = true;

  src = ./.;

  nativeBuildInputs = with pkgs; with python3Packages;
  [ pylast
    setuptools
  ];
}
