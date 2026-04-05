{
  description = "A flake for my python workspace.";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system; };
  in
  {
    devShells.${system}.default =
      pkgs.mkShell
        {
          buildInputs = [
            pkgs.uv
            pkgs.pre-commit
          ];

          shellHook = ''
            echo "Activated Nix Shell"
            uv --version
            uvx --version
          '';
        };
  };
}
