
document.addEventListener('DOMContentLoaded', () => {
	const modal = document.getElementById('id04'),
		modal1 = document.getElementById('id05'), //добавить книгу
		modal2 = document.getElementById('id08'),
		modal3 = document.getElementById('id07'),
		modal4 = document.getElementById('id06'),
		btns = document.querySelectorAll('.cncl-btn'), // кнопка отмена 
		inputValues = document.querySelectorAll('input'),
		modalCloseBtns= document.querySelectorAll('.modal__close'), // крестик
		btnId06 = document.getElementById('btnId06'),
		btnId07 = document.getElementById('btnId07'),
		btnId08 = document.getElementById('btnId08');

		
	modalCloseBtns.forEach((modalCloseBtn) => {
		modalCloseBtn.addEventListener('click', (e) =>{
			modal1.style.display = "none";
			modal.style.display = "none";
			modal2.style.display = "none";
			modal3.style.display = "none";
			modal4.style.display = "none";
			document.body.style.overflow = 'auto';
			inputValues.forEach((inputValue) =>{
				inputValue.value = '';
			});
		});
	});
		
	btns.forEach((btn) => {
		btn.addEventListener('click', (e) =>{
			modal1.style.display = "none";
			modal.style.display = "none";
			modal2.style.display = "none";
			modal3.style.display = "none";
			modal4.style.display = "none";
			document.body.style.overflow = 'auto';
			inputValues.forEach((inputValue) =>{
				inputValue.value = '';
			});
		});
	});

	btnId06.addEventListener('click', () => {
		modal.style.display = "none";
	});
	
	btnId07.addEventListener('click', () => {
		modal.style.display = "none";
	});
	
	btnId08.addEventListener('click', () => {
		modal.style.display = "none";
	});
});
