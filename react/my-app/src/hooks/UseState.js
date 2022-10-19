import React, {useState } from 'react'

const Counter = () => {
    const [count, setCount] = useState(0);

    return(
        <div>
            <button onClick={() => setCount(count + 1)}>Click para incrementar</button>
            <p>{count}</p>
        </div>
    )
}

export default Counter;