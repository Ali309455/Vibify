function get_folder(track){

}


async function test() {
    let a = await fetch(`./songs/AnuvJain/info.json`);
    let b = await a.json();
    console.log(b);
}

test();