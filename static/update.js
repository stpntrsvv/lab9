function addProduct() {
    let companyName = document.getElementById('company_name').value
    let term = document.getElementById('term').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'company_name': companyName,
                             'term': term
                             })
    })
}