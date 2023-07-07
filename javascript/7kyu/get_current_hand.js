function getCurrentHand(arr) {
    let hand = [];
    const last4 = arr.slice(arr.length - 4, arr.length);
    arr.forEach(card => {
        if(!last4.includes(card) && !hand.includes(card)) hand.push(card);
        if(hand.length == 4) return hand;
    });
    return hand;
}

function getCurrentHand2(arr) {
    return [...new Set(arr.slice(0, arr.length - 4))].filter(x => !arr.slice(-4).includes(x))
}

function getCurrentHand3(arr) {
    return [...new Set(arr.slice(0, arr.length - 4))].filter(x => !arr.slice(-4).includes(x))
}

const hand = getCurrentHand([
    'Hog Rider',
    'Earthquake',
    'Archer Queen',
    'Giant Skeleton',
    'Fire Spirit',
    'Cannon',
    'Skeletons',
    'Hog Rider',
    'The Log',
    'Fire Spirit',
    'Earthquake',
    'Giant Skeleton',
    'Skeletons',
    'Archer Queen',
    'Fire Spirit',
    'Cannon',
    'Giant Skeleton',
    'Skeletons',
  ]); // => ['Archer Queen', 'Earthquake',  'The Log', 'Hog Rider']

console.log(hand);
  