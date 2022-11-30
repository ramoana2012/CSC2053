import {useState} from 'react'
import { ProgressViewIOSComponent, Text, View, Image, Button, TextInput } from 'react-native';

const Cat = (props) => { 
  const [catGreeting, setCatGreeting] = useState("I am hungry!");
  const [isHungry, setIsHungry] = useState(true);
  const [nickname, setNickname] = useState("");
  // TO-DO: Toggle opacity of "thank you, call me" to transparent before receiving nickname

  return (
    <View>
      <Text>Hello, my name is {props.name}! {catGreeting}</Text>
      <Image
          source={{
            uri: 'https://reactnative.dev/docs/assets/p_cat2.png',
          }}
          style={{ width: 200, height: 200 }}
        />
      <TextInput
        style={{
          height: 40,
          borderColor: 'gray',
          borderWidth: 1
        }}
        defaultValue="Give me a nickname"
        onSubmitEditing={(event) => {
          setNickname(event.nativeEvent.text);

        }}
      />
      <Text>Thank you, call me {nickname}</Text>
      <Button title='Feed Me' disabled={!isHungry} 
              onPress={()=>{  setCatGreeting('Thank you!');
                              setIsHungry(false);}}/>
    </View>
  );
}

/* Cafe is the parent component and Cat is the child component */
const Cafe = (props) => {  
  return (
    <View style={{paddingTop: 100  }}>   
      <Cat name='Ruby'/>
      {/* <Cat name='Raf'/> 
      <Cat name='Bruno'/>    */}
    </View>
  );
}

export default Cafe;