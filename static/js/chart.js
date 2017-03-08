/**
 * Created by alexmwaleh on 3/8/17.
 */
var type ='polarArea';
var vector =['line','radar'];
var myChart;

$('.graph-type').on('click','button',function(){
    myChart.destroy();
    
    type = this.innerText;
    findData()

})


function findData() {
    $.ajax({
            method: 'GET',
            url: '/api/',
            cache: false,
            success: function (res) {
                console.log(res);
                var ctx = document.getElementById("myChart");
                myChart = new Chart(ctx, {
                    type: type || 'bar',
                    data: {
                        labels: res.labels,
                        datasets: [{
                            label: 'population',
                            data: res.data,
                            backgroundColor: vector.includes(type) ? res.color[1] : res.color
                        }]
                    }

                });
                window.addEventListener('resize', function () {
                    myChart.resize()
                })
            },
            error: function (err) {
                console.log(err);


            }
        }
    );
};

findData()