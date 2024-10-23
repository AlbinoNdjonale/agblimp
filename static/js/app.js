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

const constructdatetime = () => {
    const months = [
        'janeiro', 'fevereiero',
        'março', 'abril', 'junho',
        'julho', 'agosto', 'setembro',
        'outubro', 'novembro', 'dezembro'
    ]

    const datetimes = document.querySelectorAll('.datetime')

    datetimes.forEach(datetime => {
        datetime.querySelector('input').setAttribute('readonly', '')
        const calendary = document.createElement('div')
        calendary.className = 'calendary'

        const date = document.createElement('div')
        date.className = 'date'

        const header = document.createElement('div')
        const headerleft = document.createElement('div')
        const headerright = document.createElement('div')
        header.appendChild(headerleft)
        header.appendChild(headerright)
        date.appendChild(header)

        const main = document.createElement('div')
        date.appendChild(main)

        const footer = document.createElement('div')
        footer.className = 'footer'
        const button = document.createElement('button')
        button.innerText = 'ok'
        button.type = 'button'
        footer.appendChild(button)

        const divfast = document.createElement('div')

        const today    = document.createElement('span')
        today.innerText = 'hoje'
        const tomorrow = document.createElement('span')
        tomorrow.innerText = 'amanha'

        divfast.appendChild(today)
        divfast.appendChild(tomorrow)

        footer.appendChild(divfast)

        date.appendChild(footer)

        calendary.appendChild(date)

        const time = document.createElement('div')
        time.className = 'time'

        const hour = document.createElement('div')
        const min  = document.createElement('div')
        time.appendChild(hour)
        time.appendChild(min)
        calendary.appendChild(time)

        button.addEventListener('click', () => {
            datetime.querySelector('.calendary').style.display = 'none'
            main.innerHTML = ''
            hour.innerHTML = ''
            min.innerHTML  = ''
        })

        datetime.appendChild(calendary)

        const setDate = (clicked, active) => {
            active.querySelector('.active').classList.remove('active')
            clicked.classList.add('active')

            const date = datetime.querySelector('.date > div:nth-child(2) .active')
            const time = datetime.querySelectorAll('.time .active')

            const value = `${date.getAttribute('data-year')}-${date.getAttribute('data-month')}-${date.getAttribute('data-day')}T${time[0].innerText}:${time[1].innerText}`

            datetime.querySelector('input').value = value
        }

        datetime.querySelector('input').addEventListener('click', e => {
            if (datetime.querySelector('.calendary').style.display == 'flex')
                return

            const blockeds = JSON.parse(datetime.getAttribute('blockeds'))??[]

            const value = datetime.querySelector('input').value
            
            const today = new Date()
            let selectday;
            if (value == '') {
                selectday  = new Date()
            } else {
                const date = value.split('T')[0].split('-')
                const time = value.split('T')[1].split(':')
                selectday  = new Date(date[0], date[1]-1, date[2], time[0], time[1])
            }

            const start  = new Date(selectday.getFullYear(), selectday.getMonth(), 1)
        
            start.setDate(-(start.getDay()-1))

            datetime.querySelector('.calendary').style.display = 'flex'

            datetime.querySelector('.date > div:nth-child(1) > div:nth-child(1)').innerText = `${months[selectday.getMonth()-1]} de ${selectday.getFullYear()}`  

            const divday = datetime.querySelector('.date > div:nth-child(2)')
            
            for (const day of 'DSTQQSS'.split('')) {
                const element = document.createElement('span')
                element.innerText = day
                divday.appendChild(element)
            }

            for (let day = 1; day < 43; day++) {
                let date  = start.getDate()
                const element = document.createElement('span')
                element.setAttribute('data-year', start.getFullYear())
                element.setAttribute('data-month', (start.getMonth()+1 <= 9?'0':'')+(start.getMonth()+1))
                element.setAttribute('data-day', (start.getDate() <= 9?'0':'')+start.getDate())
                
                if (blockeds.includes(`${start.getFullYear()}-${start.getMonth()+1}-${start.getDate()}`)) {
                    element.classList.add('blocked')
                } else
                    element.addEventListener('click', e => setDate(e.target, divday))
    
                if (start.getMonth() !== selectday.getMonth()) element.classList.add('out')
                else if (date == selectday.getDate()) {
                    element.classList.add('active')        
                }

                if (date == today.getDate() && start.getMonth() == today.getMonth())
                    element.id = 'active'
    
                element.classList.add('date-item')
    
                element.innerText = date
                divday.appendChild(element)
                start.setDate(date + 1)
            }

            for (let hour = 0; hour < 24; hour++) {
                const element = document.createElement('span')
                if (hour == selectday.getHours()) element.classList.add('active')

                element.addEventListener('click', e => setDate(e.target, datetime.querySelector('.time > div:nth-child(1)')))
    
                element.innerText = (hour <= 9?'0':'')+hour
                datetime.querySelector('.time > div:nth-child(1)').appendChild(element)
            }

            for (let min = 0; min < 60; min++) {
                const element = document.createElement('span')
                if (min == selectday.getMinutes()) element.classList.add('active')

                element.addEventListener('click', e => setDate(e.target, datetime.querySelector('.time > div:nth-child(2)')))
    
                element.innerText = (min <= 9?'0':'')+min
                datetime.querySelector('.time > div:nth-child(2)').appendChild(element)
            }
        })

    })
}

constructdatetime()

const validatecep = async () => {
    const form = document.getElementById('scheduling')

    const cep = form.querySelector('#cep').value
    const inputs = form.querySelectorAll('input, select, button')

    if (cep.trim() == '') {
        inputs.forEach(input => input.id=='cep'?'':input.setAttribute('disabled', ''))
        form.querySelector('.err').style.display = 'block'
    } else {
        const cepvalid = await (await fetch(`validatecep/${cep}`)).json()

        if (!cepvalid.valid) {
            inputs.forEach(input => input.id=='cep'?'':input.setAttribute('disabled', ''))
            form.querySelector('.err').style.display = 'block'
        } else {
            inputs.forEach(input => input.id=='cep'?'':input.removeAttribute('disabled'))
            form.querySelector('.err').style.display = 'none'
        }
    }
}

validatecep()

const swiperbanner = new Swiper('.swiper-banner', {
    loop: true,
    
    autoplay: {
        delay: 6000,
        disableOnInteraction: false,
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

const swiper = new Swiper('.swiper-container', {
    loop: true,
    speed: 2000,
    
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
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