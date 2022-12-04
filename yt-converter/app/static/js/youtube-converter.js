const form = document.forms.url;
const urls = document.getElementById('textarea33').value;
const loader = form.querySelector('.loader');


const loardStart = () => {
  const button2 = form.querySelector('.submit_button');

  button2.addEventListener('click', function() {
    loader.style.display = 'block';
    
  }, false);
};
loardStart()


const myFunc = ()=>{
  const button = form.querySelector('button');

  button.addEventListener('click', function() {

      loader.style.display = 'block';
      console.log('javascript move!')

  }, false);
};
myFunc();
