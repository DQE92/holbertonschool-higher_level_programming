document.getElementById('add_item').onclick = () => {
    const list = document.querySelector('.my_list');
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
};
