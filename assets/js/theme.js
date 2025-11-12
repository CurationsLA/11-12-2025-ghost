/**
 * CURATIONSLA minimal front-end script
 * - Back to top button
 * - Section "↑ Back Up" links
 * (Search removed)
 */

(function(){

  /* Back To Top */
  const backTopBtn = document.querySelector('[data-back-to-top]');
  if(backTopBtn){
    backTopBtn.addEventListener('click', ()=> {
      window.scrollTo({top:0, behavior:'smooth'});
    });
    window.addEventListener('scroll', debounce(()=>{
      if(window.scrollY > 800){
        backTopBtn.classList.add('visible');
      } else {
        backTopBtn.classList.remove('visible');
      }
    },120));
  }

  /* Section Back-Up Links */
  document.addEventListener('DOMContentLoaded', ()=>{
    const anchors = document.querySelectorAll('.post-content h2[id], .post-content h3[id]');
    anchors.forEach(h=>{
      if(h.dataset.vfBackInserted) return;
      const link = document.createElement('a');
      link.href = '#top';
      link.className = 'section-back-up';
      link.textContent = '↑ Back Up';
      link.setAttribute('aria-label','Back to top');
      h.insertAdjacentElement('afterend', link);
      h.dataset.vfBackInserted = '1';
    });
  });

  /* Utilities */
  function debounce(fn, wait){
    let t; return function(...args){
      clearTimeout(t); t = setTimeout(()=>fn.apply(this,args), wait);
    };
  }

})();