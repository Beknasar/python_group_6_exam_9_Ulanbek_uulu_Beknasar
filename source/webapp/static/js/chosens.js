async function addChosen(event) {
    event.preventDefault();
    let addBtn = event.target;
    let url = addBtn.href;
    console.log(url)

    try {
        let response = await makeRequest(url, 'POST');
        let data = await response.text();
        console.log(data);
        console.log("Добавлено в избранных")
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h3>Фото добавлено в избранное.</h3>`
        setTimeout(() => note.remove(), 4000);

    }
    catch (error) {
        console.log(error);
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h3>Это фото уже в избранных</h3>`
        setTimeout(() => note.remove(), 4000);
    }
}

async function removeChoosen(event) {
    event.preventDefault();
    let removeBtn = event.target;
    let url = removeBtn.href;

    try {
        let response = await makeRequest(url, 'POST');
        let data = await response.text();
        console.log(data);
        console.log("Удалено из избранных")
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h3>Фото удалён из избранных</h3>`
        setTimeout(() => note.remove(), 3000);
    }
    catch (error) {
        console.log(error);
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h3>Фото уже удалён из избранных</h3>`
        setTimeout(() => note.remove(), 3000);
    }
}

window.addEventListener('load', function() {
    const addButtons = document.getElementsByClassName('add_chosen');
    const removeButtons = document.getElementsByClassName('remove_chosen');

    for (let btn of addButtons) {btn.onclick = addChosen}
    for (let btn of removeButtons) {btn.onclick = removeChoosen}
});