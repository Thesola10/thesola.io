{ description = "My personal website";

  inputs."nixpkgs".url = github:NixOS/nixpkgs;
  inputs."nowplaying".url = github:thesola10/thesola.io-nowplaying;
  inputs."pelicanTheme".url = github:thesola10/pelican-thesola.io;
  inputs."pelicanTheme".flake = false;

  outputs = { self, nixpkgs, flake-utils, pelicanTheme, ... }:
  flake-utils.lib.eachDefaultSystem
    (system:
    let pkgs = import nixpkgs { inherit system; };
    in rec
    { packages.default = pkgs.callPackage ./. { inherit pelicanTheme; };
      packages.publish = pkgs.callPackage ./. { inherit pelicanTheme; publish = true; };
      devShells.default = pkgs.mkShell {
        inputsFrom = [ packages.default ];
        packages = with pkgs; [ darkhttpd ];
        buildInputs = with pkgs.python3Packages; [
          venvShellHook
        ];

        venvDir = ".venv";
      };
    });
}
