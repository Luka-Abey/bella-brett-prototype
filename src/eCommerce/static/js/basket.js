var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
  updateBtns[i].addEventListener('click', function(){
    var itemId = this.dataset.item
    var action = this.dataset.action
    console.log(itemId, action)
  })
}