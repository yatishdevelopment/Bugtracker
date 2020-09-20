var app = angular.module('myApp',[]);

app.controller('myCtrl',function($scope){
    $scope.signUp = function(){
        $("#msg").hide()
        $("#signUpModal").modal('show')
        $("input#id_name").on({
        keydown: function(e) {
                if (e.which === 32)
                  return false;
                },
            });
        $("input#id_password").on({
        keydown: function(e) {
                if (e.which === 32)
                  return false;
                },
            });
    },
    $scope.signIn = function(){
        $("#msg_login").hide()
        $("#signInModal").modal('show')
    },
    
    $scope.submitData = function(){
        if ($('#id_name').val() == '' || $('#id_password').val()== '' ){
            $("#msg").html('All Fields Required')
            $("#msg").show()
            return false
        }
        $.ajax({
            type: 'POST',
            url: 'employee/',
            data: {
                username:$('#id_name').val(),
                password:$('#id_password').val(),
            },
            dataType: 'json',
            success: function (data) {
                $("#msg").html(data.msg)
                $("#msg").show()

                if(data.code==1){
                    $("#msg").attr('class','alert alert-success text-center')
                    $("#msg").show()
                    $('#signUpModal form')[0].reset();
                    setTimeout(function() { $("#signUpModal").modal('hide'); }, 1000)
                }                

            }
        });
    },

    $scope.allProjects = function(){
        $("#allProjectsModal").modal("show")
    }


})