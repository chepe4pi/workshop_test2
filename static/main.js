window.onload = function () {
    new Vue({
        el: '#app',
        created: function () {
            axios.get('/songs/')
                .then(function (response) {
                    console.log(response.data)
                })
        }
    });
}