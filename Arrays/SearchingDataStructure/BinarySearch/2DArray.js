/*

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

*/

// BruteForce Approach

function findingElemInMatrix(matrix,searchVal){
    let rows = matrix.length
    let columns = matrix[0].length

    for(let i=0;i<rows;i++){
        for(let j=0;j<columns;j++){
            if(matrix[i][j]===searchVal){
                return true
            }
        }
    }
    return false
    
}
const matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

 
const searchValue = 5

const result = findingElemInMatrix(matrix,searchValue)
console.log(result)
