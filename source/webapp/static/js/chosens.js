async function addChosen(event) {
    event.preventDefault();
    let addBtn = event.target;
    let url = addBtn.href;
    console.log(url)

    try {
        let response = await makeRequest(url, 'POST');
        let data = await response.text();
        console.log(data);
        console.log("Добавлено в избранное")
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #155724">Фото добавлено в избранное.</h6>`
        setTimeout(() => note.remove(), 4000);

    }
    catch (error) {
        console.log(error);
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #721c24">Это фото уже в избранных</h6>`
        setTimeout(() => note.remove(), 4000);
    }
}

async function removeFavorite(event) {
    event.preventDefault();
    let likeBtn = event.target;
    let url = likeBtn.href;

    try {
        await makeRequest(url, 'POST');
        console.log("Удалено из избранного")
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #155724">Фото удалён из избранных</h6>`
        setTimeout(() => note.remove(), 3000);
    }
    catch (error) {
        console.log(error);
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #721c24">Фото уже удалён из избранных</h6>`
        setTimeout(() => note.remove(), 3000);
    }
}

window.addEventListener('load', function() {
    const addButtons = document.getElementsByClassName('add_chosen');
    // const removeButtons = document.getElementsByClassName('remove_fav');

    for (let btn of addButtons) {btn.onclick = addChosen}
    // for (let btn of removeButtons) {btn.onclick = removeFavorite}
});