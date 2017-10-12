
//var Datastore = require('nedb')


var app = angular.module('myApp', ['ui.bootstrap']);

app.controller('PosController', function ($scope, $http,$modal) {

    $scope.drinks = [{
        id: 0,
        name: "Still Water",
        price: "1",
    },
    {
        id: 1,
        name: "Sparkling Water",
        price: "10",
    },
    {
        id: 2,
        name: "Espresso",
        price: "12",
    },
    {
        id: 3,
        name: "Cappuccino",
        price: "13",
    },
    {
        id: 4,
        name: "Tea",
        price: "19",
    },
    {
        id: 5,
        name: "Hot Chocolate",
        price: "21",
    },
    {
        id: 6,
        name: "Coke",
        price: "20",
    },
    {
        id: 7,
        name: "Orange Juice",
        price: "90",
    }];

    $scope.foods = [{
        id: 8,
        name: "Waffle",
        price: "50",
    },
    {
        id: 9,
        name: "Brioche",
        price: "130",
    },
    {
        id: 10,
        name: "Cheesecake",
        price: "0",
    },
    {
        id: 11,
        name: "Sandwich",
        price: "20",
    },
    {
        id: 12,
        name: "Donuts",
        price: "190",
    },
    {
        id: 13,
        name: "Tortilla",
        price: "19",
    }];

    $scope.order = [];
    $scope.new = {};
    $scope.totOrders = 0;

    var url = window.location.protocol + "://" + window.location.host + "/" + window.location.pathname;

    $scope.getDate = function () {
        var today = new Date();
        var mm = today.getMonth() + 1;
        var dd = today.getDate();
        var yyyy = today.getFullYear();

        var date = dd + "/" + mm + "/" + yyyy

        return date
    };

    $scope.addToOrder = function (item, qty) {
        var flag = 0;
        if ($scope.order.length > 0) {
            for (var i = 0; i < $scope.order.length; i++) {
                if (item.id === $scope.order[i].id) {
                    item.qty += qty;
                    flag = 1;
                    break;
                }
            }
            if (flag === 0) {
                item.qty = 1;
            }
            if (item.qty < 2) {
                $scope.order.push(item);
            }
        } else {
            item.qty = qty;
            $scope.order.push(item);
        }
    };

    $scope.removeOneEntity = function (item) {
        for (var i = 0; i < $scope.order.length; i++) {
            if (item.id === $scope.order[i].id) {
                item.qty -= 1;
                if (item.qty === 0) {
                    $scope.order.splice(i, 1);
                }
            }
        }
    };

    $scope.removeItem = function (item) {
        for (var i = 0; i < $scope.order.length; i++) {
            if (item.id === $scope.order[i].id) {
                $scope.order.splice(i, 1);
            }
        }
    };

    $scope.getTotal = function () {
        var tot = 0;
        for (var i = 0; i < $scope.order.length; i++) {
            tot += ($scope.order[i].price * $scope.order[i].qty)
        }
        return tot;
    };

    $scope.clearOrder = function () {
        $scope.order = [];
    };

    $scope.checkout = function (index) {
        /*alert($scope.getDate() + " - Order Number: " + ($scope.totOrders+1) + "\n\nOrder amount: $" + $scope.getTotal().toFixed(2) + "\n\nPayment received. Thanks.");
        $scope.order = [];
        $scope.totOrders += 1;*/
	/*	var receipt_h = web3.eth.getTransactionReceipt(index, function(err, transactionHash) {
  if (!err)
  {console.log(transactionHash.blockNumber); // "0x7f9fade1c0d57a7af66ab4ead7c2eb7b11a91385"
		alert("Transaction confirmed at block:" +transactionHash.blockNumber+"transaction id"+transactionHash);
		 $scope.order = [];
        $scope.totOrders += 1;
  }} );*/
		//alert(receipt_h.blockNumber);
	console.log($scope.getTotal());/*.toFixed(2));*/
	$http.get('/send?total='+$scope.getTotal()).then(function(response) {
	$scope.receipt = response.data.receipt;
	alert('tx hash'+response.data.receipt);
	console.log(response.data.receipt);
	/*$scope.order = [];
    $scope.totOrders += 1;
    */});
	}
    $scope.addNewItem = function (item) {
        if (item.category === "Drinks") {
            item.id = $scope.drinks.length + $scope.foods.length
            $scope.drinks.push(item)
            $scope.new = []
            $('#myTab a[href="#drink"]').tab('show')
        } else if (item.category === "Foods") {
            item.id = $scope.drinks.length + $scope.foods.length
            $scope.foods.push(item)
            $scope.new = []
            $('#myTab a[href="#food"]').tab('show')
        }
    };
	   $scope.open = function () {
                var modalInstance = $modal.open({
					controller: 'PopupCont',
                    templateUrl: 'Popup.html',
                });
            };
		 
});


       angular.module('myApp').controller('PopupCont', ['$scope','$modalInstance',function ($scope, $modalInstance) {
            $scope.close = function () {
                $modalInstance.dismiss('cancel');
            };
        }]);
  