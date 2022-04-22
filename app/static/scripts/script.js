todos=$('.todos')

inputText = $('.input input')
inputText.keypress('click',(e)=>{
    key=e.which;
    if (key==13){
        console.log('Sending new data input')
        console.log(e.target)

        return false
    }
})
inputButton = $('.input .input-button')
inputButton.on('click',(e)=>{
    console.log('Sending new data input')
    console.log(e)

})

deleteButtons = document.querySelectorAll('.delete')
deleteButtons.forEach(element=> {
    element.addEventListener('click',(e)=>{
        console.log(e.target)
        console.log(element,'test')
        console.log('button')
    })
});

editButtons = document.querySelectorAll('.edit')
editButtons.forEach(function(button)  {
    button.addEventListener('click',(e)=>{
        console.log(button)
        console.log(e.target)
        console.log('button')
    })
});

timeButtons = document.querySelectorAll('.time')
timeButtons.forEach(function(button)  {
    button.addEventListener('click',(e)=>{
        console.log(e.target)
        console.log('button')
    })
});