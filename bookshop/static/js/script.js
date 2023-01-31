

document.addEventListener('DOMContentLoaded', () => {
	const modal = document.getElementById('id01'),
		modal1 = document.getElementById('id02'),
		modal2 = document.getElementById('id03'),
		btns = document.querySelectorAll('.clear'),
		inputValues = document.querySelectorAll('input'),
		accountRegistration = document.getElementById('accountRegistration'),
		toComeInAccount = document.getElementById('toComeInAccount'),
		modalCloseBtns= document.querySelectorAll('.modal__close'), // крестик
		forgotRegistration = document.getElementById('forgotRegistration'),
		forgotYourPassword = document.getElementById('forgotYourPassword');

	
	forgotRegistration.addEventListener('click', () => {
		modal1.style.display = "none";
	});

	forgotYourPassword.addEventListener('click', () => {
		modal1.style.display = "none";
	});

	btns.forEach((btn) => {
		btn.addEventListener('click', (e) =>{
			modal1.style.display = "none";
			modal2.style.display = "none";
			modal.style.display = "none";
			inputValues.forEach((inputValue) =>{
				inputValue.value = '';
			});
		});
	});

			
	modalCloseBtns.forEach((modalCloseBtn) => {
		modalCloseBtn.addEventListener('click', (e) =>{
			modal1.style.display = "none";
			modal.style.display = "none";
			modal2.style.display = "none";
			document.body.style.overflow = 'auto';
			inputValues.forEach((inputValue) =>{
				inputValue.value = '';
			});
		});
	});


// Когда пользователь щелкает в любом месте за пределами модального окна, 
// то необходимо закрыть его.
/*  	window.addEventListener('onclick', (event) => {
		 */
		/* if (event.target.id == modal) {
			console.log('1 modal wimdow');
			modal1.style.display = "none";
			modal2.style.display = "none";
		} else if (event.target == modal1) {
			console.log('2 modal wimdow');
			modal.style.display = "none";
			modal2.style.display = "none";
		} else if (event.target == modal2) {
			console.log('3 modal wimdow');
			modal1.style.display = "none";
			modal2.style.display = "none";
		} */
		


	/* window.onclick = function(event) {
    if(event.target == modal||event.target == modal1||event.target == modal2){
        modal.style.display = "none";
				modal1.style.display = "none";
				modal2.style.display = "none";
    } 
		
}; */
});







/* const inputData = document.querySelectorAll('.form-control'),
			btnSuccess = document.querySelector('.btn-outline-success');


btnSuccess.addEventListener('click', () => {
	const firstName = document.getElementById('first-name').value,
			secondName = document.getElementById('second-name').value,
			link = document.getElementById('link').value,
			username = document.getElementById('username').value;

	console.log(firstName);
}); */


/* let modal = $modal({
	title: 'Registration'
});

  // при клике на документ
document.addEventListener('click', function(e) {
  if (e.target.dataset.toggle === 'modal') {
    modal.show();
  }
});
 */
/* 
const btns = document.querySelectorAll('button');
btns.forEach((e) => {
	e.addEventListener('click', () => {
		console.log("i click");
	});
}); */