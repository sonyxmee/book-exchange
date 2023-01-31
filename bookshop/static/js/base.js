
document.addEventListener('DOMContentLoaded', () => {
	const modal = document.getElementById('id01'),
		btns = document.querySelectorAll('.clear'),
		inputValues = document.querySelectorAll('input'),
		modalCloseBtns= document.querySelectorAll('.modal__close'); // крестик


	btns.forEach((btn) => {
		btn.addEventListener('click', (e) =>{
			modal.style.display = "none";
			inputValues.forEach((inputValue) =>{
				inputValue.value = '';
			});
		});
	});

	modalCloseBtns.forEach((modalCloseBtn) => {
		modalCloseBtn.addEventListener('click', (e) =>{
			modal.style.display = "none";
			document.body.style.overflow = 'auto';
			inputValues.forEach((inputValue) =>{
				inputValue.value = '';
			});
		});
	});

});
