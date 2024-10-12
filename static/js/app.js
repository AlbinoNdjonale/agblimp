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
    const service = document.querySelector(`div[data-id='${id}']`)

    const learn_more_service = document.querySelector('.learn-more-service')
    learn_more_service.querySelector('h2').innerText = service.getAttribute('data-name')
    learn_more_service.querySelector('p').innerText = service.getAttribute('data-description')
    learn_more_service.style.display = 'flex'
    learn_more_service.querySelectorAll('button')[1].addEventListener('click', () => to_scheduling_servie(id))
}

const to_scheduling_servie = (id) => {
    document.getElementById('service').value = id
    close_context('.learn-more-service')
    document.getElementById('link-home').click()
}
