def ping_pong(sounds):
    sounds = sounds.split('-')
    ping, pong = 0, 0
    last = sounds[0]
    serve = last
    for i in range(1, len(sounds)):
        sound =  sounds[i]
        if not sound in ("ping", "pong"):
            if sound != serve:
                if serve == "ping":
                    ping += 1
                elif serve == "pong":
                    pong += 1
            else:
                if last == "ping":
                    pong += 1
                elif last == "pong":
                    ping += 1
            if i + 1 < len(sounds) and sounds[i + 1] in ("ping", "pong"):
                serve = sounds[i + 1]
        else:
            last = sound
        print(f"Ping: {ping} Pong: {pong} Current: {sound}")
    print(f"Last: {last}")
    if ping == pong:
        return serve
    elif ping > pong:
        return "ping"
    else:
        return "pong"

noises1 = "ping-pong-ping-pong-bonk-bing-doof" # ping
noises2 = "pong-ping-dong-ping-pong-tink-bonk-pong-ping-doof" # pong
noises3 = "pong-ping-bink-ping-pong-donk" # ping
noises4 = 'ping-pong-aaaa-ping-pong-ping-aaaa' # ping
noises5 = 'pong-ping-pong-donk-pong-ping-pong-donk-pong-ping-pong-doof-pong-ping-donk' # pong
noises6 = 'ping-pong-ping-voom-wizz-ping-wizz-ping-pong-ping-pong-ping-pong-foom-bang-plop-pong-ping-pong-ping-pong-ping-pong-ping-pong-ping-klak-bing'# pong
print(ping_pong(noises6))