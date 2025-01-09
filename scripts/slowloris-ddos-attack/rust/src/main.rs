mod cli;
use cli::Args;

fn main() {
    let args = Args::parse_args();
    let ip = args.ip();    
    let port = args.port();
    let num_connections = args.num_connections().unwrap_or(200);

    let result = rust::slowloris(ip, port, num_connections);
    println!("{:#?}", result);
}

