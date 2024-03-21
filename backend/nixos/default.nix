{ pkgs, config, lib, ... }:
#
# Default service module for this API server
#

let
  cfg = config.services.thesola-io-api;
in
{
options.services.thesola-io-api = with lib; {
  enable = mkEnableOption "thesola.io API server.";

  host = mkOption {
    type = types.str;
    description = "HTTP host to listen on.";
    default = "0.0.0.0";
  };

  port = mkOption {
    type = types.int;
    description = "HTTP port to listen on.";
    default = 5000;
  };

  package = mkOption {
    type = types.package;
    description = "The API server package to use.";
    default = pkgs.thesola-io-api;
  };

  envFile = mkOption {
    type = types.str;
    description = "Path to the file containing environment variables and secrets.";
    example = "/srv/thesola-io-api/env.txt";
  };
};

config.nixpkgs.overlays =
  [ (final: prev: { thesola-io-api = prev.callPackage ./.; }) ];

config.services = lib.mkIf cfg.enable
{ uwsgi.enable = true;
  uwsgi.instance.type = "emperor";
  uwsgi.instance.vassals = {
      "thesola-io-api" = {
        type = "normal";
        pythonPackages = self: with self; [ cfg.package ];
        socket = "${cfg.host}:${builtins.toString cfg.port}";
        module = "thesola_io_api.wsgi";
        env = "@(${cfg.envFile})";
      };
  };
};
}
