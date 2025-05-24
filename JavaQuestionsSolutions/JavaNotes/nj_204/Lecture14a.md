# Object downcast example

```java
class Demo 
{
	public static void main(String[] args) 
	{
		// same class variable and same class object
		//LgOldTv remote = new LgOldTv();

		//remote.start();
		//remote.increaseVolume();
		// remote.changeChannel();// old way

		//LgSmartTv remote = new LgSmartTv();
		//remote.start();
		//remote.increaseVolume();
		//remote.changeChannel();// smart way
		//remote.playGame();
		
		// same or child class object
		LgOldTv remote = new LgSmartTv();
		remote.start();
		remote.increaseVolume();
		remote.changeChannel();// smart way i.e. over ridden method
		//remote.playGame();

		//LgSmartTv sremote = new LgSmartTv();
		//sremote.playGame();
		// why you want to create two object of same class
		// in the memeory

		// so use object downcast

		LgSmartTv sremote = (LgSmartTv)remote;// here we are 
		// downcast parent reference variable to  child and 
		// then accessing child methods.
		sremote.playGame();


	}
}
```

```java
class LgOldTv extends Object
{

	public void start(){
		System.out.println("TV starting");
	}
	public void increaseVolume(){
		System.out.println("Volume increased");
	}

	public void changeChannel(){
		System.out.println("Channel changed in old way");
	}

	public static void main(String[] args) 
	{
		System.out.println("Hello World!");
	}
}
```

```java
class  LgSmartTv extends LgOldTv
{
	@Override
	public void changeChannel(){
		System.out.println("Change channel in smart way");
	}

	// It can have it's own method
	public void playGame(){
		System.out.println("Game starts");
	}
}
```