function bindEventCaptchaClick(){
    $('#captcha-btn').click(function (event) {
        var $this = $(this)
        event.preventDefault();
        var email = $('#exampleInputEmail1').val();
        $.ajax({
            url: '/auth/captcha/email?email=' + email,
            methd: 'GET',
            success: function (result) {
                var code = result['code']
                if (code == 200) {
                    var countdown = 5;
                    $this.off('click')
                    var timer = setInterval(function () {
                        $this.text(countdown);
                        countdown -= 1;
                        if (countdown <= 0) {
                            clearInterval(timer);
                            $this.text('获取验证码')
                            bindEventCaptchaClick()
                        }
                    },1000)
                }
                console.log(result)
            },
            fail: function (error) {
                console.log(error)
            }
        })
    })
}
$(function () {
    bindEventCaptchaClick();
})