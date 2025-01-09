use clap::Parser;

#[derive(Parser, Debug)]
#[command(
    version="0.1.0", 
    about="Command-line Slowloris DDoS attack",
    long_about = None)]
pub struct Args {
    #[arg(short='i',
        long="ip",
        help="IP/Host")]
    ip: String,
    #[arg(short='p',
        long="port",
        help="Port connection")]
    port: u16,
    #[arg(short='n',
        long="num_connections",
        default_value="200",
        help="number of connections, default 200 connections")]
    num_connections: Option<u16>
}

impl Args {
    pub fn parse_args() -> Self {
        Self::parse()
    }
    pub fn default(ip: String, port: u16) -> Self {
        Self {
            ip,
            port,
            num_connections: Some(200)
        }
    }

    pub fn ip(&self) -> &str {
        &self.ip
    }
    pub fn port(&self) -> u16 {
        self.port
    }
    pub fn num_connections(&self) -> Option<u16> {
        self.num_connections
    }
    pub fn set_num_connections(&mut self, num: u16) {
        self.num_connections = Some(num)
    }
}
