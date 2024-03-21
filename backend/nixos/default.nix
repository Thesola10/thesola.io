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
    default = import ../.;
  };

  envFile = mkOption {
    type = types.str;
    description = "Path to the file containing environment variables and secrets.";
    example = "/srv/thesola-io-api/env.txt";
  };
};

config = lib.mkIf cfg.enable
{ systemd.services."thesola-io-uwsgi" =
  { description = "thesola.io API server";
    path = with pkgs; [ cfg.package uwsgi ];
    serviceConfig =
    { ExecStart = "";
      EnvironmentFile = cfg.envFile;
    };
    wantedBy = [ "default.target" ];
    enable = true;
  };
};
}
