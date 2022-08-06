// import * as tf from '@tensorflow/tfjs';
// import '@tensorflow/tfjs-backend-webgl';


function main(){

    console.log(tf.getBackend());

    tf.setBackend('webgl'); /// available options 'wasm' 'cpu', 'webgl'
    // tf.ready().then(() => {});

    console.log(JSON.stringify(tf.getBackend()))


    const myArr = [1, 2, 3, 4, 5, 6];
    const shape = [2, 3];
    const tensorA = tf.tensor(myArr, shape);
    document.getElementById("demo").innerHTML = tensorA;
    console.log(tensorA);
    tensorA.print();

    const A = tf.randomNormal([10, 1000]);
    const W = tf.randomNormal([1000, 500]);

    var startTime = performance.now()
    var C = tf.matMul(A, W)
    var endTime = performance.now()


    C.print()
    tf.print(C.shape);
    document.getElementById("demo").innerHTML += " :"+C.shape
    document.getElementById("demo").innerHTML += " Mils:"+(endTime-startTime)



}

main();