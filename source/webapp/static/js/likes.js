async function addFavorite(event) {
    event.preventDefault();
    let likeBtn = event.target;
    let url = likeBtn.href;

    try {
        await makeRequest(url, 'POST');
        console.log("Добавлено в избранное")
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #155724">Вы добавили фото в избранное.</h6>`
        note.classList.add('mx-4', 'mx-4', 'px-3', 'py-2', 'note_success')
        setTimeout(() => note.remove(), 3000);

    }
    catch (error) {
        console.log(error);
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #721c24">Вы уже добававили это фото в избранное!</h6>`
        note.classList.add('mx-4', 'mx-4', 'px-3', 'py-2', 'note_danger')
        setTimeout(() => note.remove(), 3000);
    }
}

async function onUnlike(event) {
    event.preventDefault();
    let unlikeBtn = event.target;
    let url = unlikeBtn.href;

    try {
        let response = await makeRequest(url, 'DELETE');
        let data = await response.text();
        console.log(data);
        const counter = unlikeBtn.parentElement.getElementsByClassName('counter')[0];
        counter.innerText = data;
    }
    catch (error) {
        console.log(error);
    }

    unlikeBtn.classList.add('hidden');
    const likeBtn = unlikeBtn.parentElement.getElementsByClassName('like')[0];
    likeBtn.classList.remove('hidden');
}

window.addEventListener('load', function() {
    const likeButtons = document.getElementsByClassName('like');
    const unlikeButtons = document.getElementsByClassName('unlike');

    for (let btn of likeButtons) {btn.onclick = onLike}
    for (let btn of unlikeButtons) {btn.onclick = onUnlike}
});
