const requires = JSON.parse(JSON.parse(document.getElementById('requires').textContent))

// deleting querys params of url
const urlSemQueryParams = window.location.protocol + "//" + window.location.host + window.location.pathname;
window.history.replaceState({}, document.title, urlSemQueryParams);

// function to close popup's
const close_context = (id) => {
    const msg = document.querySelector(id)
    msg.style.display = 'none'
}


const set_service_description = () => {
    const services = document.querySelectorAll('.service')

    services.forEach(service => {
        const description = service.getAttribute('data-description')
        service.querySelector('p').innerText = description.slice(0, 50)+(description.length>50?'...':'')
    })
}
set_service_description()

const display_learn_more_servie = (id) => {
    const service = document.querySelector(`div[data-id='${id}'].service`)

    const learn_more_service = document.querySelector('.learn-more-service')
    learn_more_service.querySelector('h2').innerText = service.getAttribute('data-name')
    learn_more_service.querySelector('p').innerText = service.getAttribute('data-description')
    learn_more_service.querySelector('img').src = service.getAttribute('data-image')
    learn_more_service.style.display = 'flex'
    learn_more_service.querySelectorAll('button')[1].addEventListener('click', () => to_scheduling_servie(id))
}

const display_learn_more_jobopening = (id) => {
    const jobopening = document.querySelector(`div[data-id='${id}'].jobopening`)

    const learn_more_jobopening = document.querySelector('.learn-more-jobopening')
    learn_more_jobopening.querySelector('h2').innerText = jobopening.getAttribute('data-title')
    learn_more_jobopening.querySelectorAll('p')[0].innerText = jobopening.getAttribute('data-description')
    learn_more_jobopening.querySelectorAll('p')[1].innerText = 'Salario R$ '+jobopening.getAttribute('data-salary')+',00'
    learn_more_jobopening.querySelector('ul').innerHTML = requires.map(require => {
        if (require.fields.jobopening == jobopening.getAttribute('data-id'))
            return '<li>'+require.fields.title+(require.fields.required?'':' (opcional)')+'</li>'
        return ''
    }).join('')
    learn_more_jobopening.style.display = 'flex'
    learn_more_jobopening.querySelectorAll('button')[1].addEventListener('click', () => to_candidate_jobopening(id))
}

const to_scheduling_servie = (id) => {
    document.getElementById('service').value = id
    document.getElementById('cep').focus()
    close_context('.learn-more-service')
}

const to_candidate_jobopening = (id) => {
    document.getElementById('job').value = id
    close_context('.learn-more-jobopening')
    document.getElementById('link-form-job').click()
    document.getElementById('fullname').focus()
}

const expand = () => {
    const menu = document.getElementById('menu-mobile')

    const state = menu.style.width

    menu.style.width = state==='80vw'?'0':'80vw'
}

document.querySelectorAll('#menu-mobile a')
    .forEach(item => item.addEventListener('click', expand))

const filter = (filter, item_class, tag_content) => {
    const has_comon_word = (string1, string2) => {
        const words = string1.toLowerCase().trim().split(' ')
    
        for (const word of words)
            if (string2.toLowerCase().includes(word))
                return true
    }

    const nocomon_word = (string1, string2) => {
        const words = string1.toLowerCase().trim().split(' ')

        let count = 0
        for (const word of words)
            if (!string2.toLowerCase().includes(word))
                count++

        return count
    }
    
    const faqs = document.querySelectorAll('.'+item_class)
    faqs.forEach(item => {
        const question = item.querySelector(tag_content).innerText

        if (has_comon_word(filter, question) && nocomon_word(filter, question) <= 2) {
            item.style.display = 'block'
        } else {
            item.style.display = 'none'
        }

    })
}

const swiper = new Swiper('.swiper-container', {
    loop: true, // Permite que o carrossel seja contínuo
    speed: 2000,
    
    autoplay: {
        delay: 5000, // Tempo de exibição de cada slide (em milissegundos)
        disableOnInteraction: false, // Continua a auto rotação após interação
    },

    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
});

const acceptcookie = () => {
    document.cookie = 'can_use_cookie=true; max_age=' + (60 * 60 * 24 * 30) + '; path=/'
    document.getElementById('banner-cookie').style.display = 'none'
}

const checkcookie = () => {
    if (!document.cookie.split(';').some((item) => item.trim().startsWith('can_use_cookie='))) {
        document.getElementById('banner-cookie').style.display = 'block';
    }
}

checkcookie()