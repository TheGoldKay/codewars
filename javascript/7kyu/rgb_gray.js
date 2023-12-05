function rgbToGrayscale(color){
    let R = color.substring(1, 3);
    let G = color.substring(3, 5);
    let B = color.substring(5, 7);
    R = parseInt(R, 16);
    G = parseInt(G, 16);
    B = parseInt(B, 16);
    let y = Math.round(0.299 * R + 0.587 * G + 0.114 * B);
    let gray = y.toString(16).toUpperCase().padStart(2, '0');
    return `#${gray.repeat(3)}`;
}

console.log(rgbToGrayscale("FFFFFF"));